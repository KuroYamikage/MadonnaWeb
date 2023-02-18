{ pkgs ? import <nixpkgs> { } }:

with pkgs;

mkShell {
  buildInputs =
    [ python3 python3Packages.django python3Packages.django-debug-toolbar ];
}
