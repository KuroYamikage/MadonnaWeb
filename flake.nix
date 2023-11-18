{
  description = "MadonnaWeb";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; })
          mkPoetryEnv defaultPoetryOverrides;
        pypkgs-build-requirements = {
          sqlparse = [ "flit" ];
          urllib3 = [ "hatchling" ];
          django-recaptcha = [ "setuptools" ];
          django-session-timeout = [ "setuptools" ];
          contourpy = [ "meson-python" ];
          pandas = [ "meson-python" ];
          lunardate = [ "setuptools" ];
          pyluach = [ "flit" ];
          sqlite3-0611 = [ "setuptools" ];
          workalendar = [ "setuptools" ];
        };
        p2n-overrides = defaultPoetryOverrides.extend (self: super:
          builtins.mapAttrs (package: build-requirements:
            (builtins.getAttr package super).overridePythonAttrs (old: {
              buildInputs = (old.buildInputs or [ ]) ++ (builtins.map (pkg:
                if builtins.isString pkg then
                  builtins.getAttr pkg super
                else
                  pkg) build-requirements);
            })) pypkgs-build-requirements);
      in {
        packages = {
          myapp = mkPoetryEnv {
            projectDir = ./.;
            overrides = p2n-overrides;
          };
        };

        defaultPackage = self.packages.${system}.myapp;

        devShells.default = pkgs.mkShell {
          buildInputs = [
            pkgs.poetry
            self.packages.${system}.myapp
            pkgs.redis
            pkgs.sqlite
          ];
        };
      });
}
