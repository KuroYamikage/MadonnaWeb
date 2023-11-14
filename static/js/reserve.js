document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar')
    var selectedCheckInDate = null
    var selectedCheckOutDate = null
    var form = document.getElementById('multi-step-form')

    // Define the unavailableDates array with date strings in "Sept 21, 2023" format


    // Create an array to store the converted unavailable events
    const unavailableEvents = [];

    // Function to convert date string to ISO format
   // Function to convert date string to ISO format
		function convertToDateISO(dateStr) {
			const dateParts = dateStr.split(' ');
			if (dateParts.length === 3) {
				const month = dateParts[0];
				const day = dateParts[1].replace(',', '');
				const year = dateParts[2];
				const isoDate = new Date(`${month} ${day}, ${year} 00:00:00 UTC`);
				return isoDate.toISOString().split('T')[0];
			}
			return null; // Handle invalid date format
		}
	
		// Convert and create unavailableEvents
		unavailableDates.forEach(function (dateInfo) {
            const isoDate = convertToDateISO(dateInfo.date);
            if (isoDate) {
                if (dateInfo.pool1) {
                    unavailableEvents.push({
                        title: 'Pool 1 Unavailable',
                        start: isoDate,
                        rendering: 'background',
                        color: 'red'
                    });
                }
                if (dateInfo.pool2) {
                    unavailableEvents.push({
                        title: 'Pool 2 Unavailable',
                        start: isoDate,
                        rendering: 'background',
                        color: 'yellow'
                    });
                }
            }
        });

    const stepContainer = document.querySelector('.container')
    const steps = document.querySelectorAll('.step')
    const prevStepButton = document.getElementById('prev-step')
    const nextStepButton = document.getElementById('next-step')
    const submitReservationButton = document.getElementById('submit-reservation')
    const reservationTimeDropdown = document.getElementById('id_reservation_time')
    const checkInDateField = document.getElementById('id_check_in_date')
    const checkOutDateField = document.getElementById('id_check_out_date')
    const checkInTimeField = document.getElementById('id_check_in_time')
    const checkOutTimeField = document.getElementById('id_check_out_time')
    const reservationTypeSelect = document.getElementById("id_reservation_type");


    console.log(unavailableEvents)
    // Add an event listener to the reservation_time dropdown
    reservationTimeDropdown.addEventListener('change', function () {
        const selectedReservationTime = reservationTimeDropdown.value

        // Get today's date
        const today = new Date(checkInDateField.value)
        const tomorrow = new Date(today)
        tomorrow.setDate(today.getDate() + 1) // Calculate tomorrow's date

        if (selectedReservationTime === 'Morning') {
            // For Morning reservation, set check-in at 7:00 AM and check-out at 7:00 PM on the same day
            checkInDateField.value = formatDate(today) // Format today's date
            checkOutDateField.value = formatDate(today) // Format today's date
            checkInTimeField.value = '07:00 AM'
            checkOutTimeField.value = '05:00 PM'
        } else if (selectedReservationTime === 'Night') {
            // For Night reservation, set check-in at 7:00 PM and check-out at 7:00 AM (next day)
            checkInDateField.value = formatDate(today) // Format today's date
            checkOutDateField.value = formatDate(tomorrow) // Format tomorrow's date
            checkInTimeField.value = '05:00 PM'
            checkOutTimeField.value = '07:00 AM'
        }else if (selectedReservationTime === '22 Hours'){
            // For Night reservation, set check-in at 7:00 PM and check-out at 7:00 AM (next day)
            checkInDateField.value = formatDate(today) // Format today's date
            checkOutDateField.value = formatDate(tomorrow) // Format tomorrow's date
            checkInTimeField.value = '07:00 AM'
            checkOutTimeField.value = '05:00 PM'
        }
        
    })



    // Add an event listener to the "Next" button
    nextStepButton.addEventListener('click', function () {
        convertAndSetTimeFormat(false) // Pass false to indicate going to the next step
    })

    // Add an event listener to the "Previous" button
    prevStepButton.addEventListener('click', function () {
        convertAndSetTimeFormat(true) // Pass true to indicate going to the previous step
    })

    function convertAndSetTimeFormat(isPrevious) {
        const check_in = document.getElementById('id_check_in_time') // Replace with your actual field ID
        const check_inValue = check_in.value
        const newCheckInTime = convertTimeFormat(check_inValue, isPrevious)

        const check_out = document.getElementById('id_check_out_time') // Replace with your actual field ID
        const check_outValue = check_out.value
        const newCheckOutTime = convertTimeFormat(check_outValue, isPrevious)

        // Update the input values with the new time format
        check_in.value = newCheckInTime
        check_out.value = newCheckOutTime
    }

    function convertTimeFormat(inputTime, isPrevious) {
        let result = inputTime // Use let instead of const

        if (isPrevious) {
            // If going to the previous step, convert the time format back to "7:00 AM"
            const timeParts = inputTime.split(':')
            if (timeParts.length === 3) {
                let hours = parseInt(timeParts[0])
                const minutes = parseInt(timeParts[1])
                const period = hours < 12 ? 'AM' : 'PM'
                hours = hours % 12 || 12 // Convert 0 to 12 for AM
                result = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')} ${period}`
            }
        } else {
            // If going to the next step, convert the time format to "7:00:00"
            const timeParts = inputTime.split(' ')
            if (timeParts.length === 2) {
                const time = timeParts[0]
                const period = timeParts[1].toUpperCase()

                let hours = parseInt(time.split(':')[0])
                const minutes = parseInt(time.split(':')[1])

                if (period === 'PM' && hours !== 12) {
                    hours += 12
                } else if (period === 'AM' && hours === 12) {
                    hours = 0
                }
                result = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:00`
            }
        }

        return result // Return the updated result
    }

    function isToday(dateStr) {
        var today = new Date()
        var selectedDate = new Date(dateStr)
        return today.getDate() === selectedDate.getDate() && today.getMonth() === selectedDate.getMonth() && today.getFullYear() === selectedDate.getFullYear()
    }
    // Handle the click event for the "Clear" button
    const clearCheckInButton = document.getElementById('clearCheckIn')
    clearCheckInButton.addEventListener('click', function () {
        // Clear the check-in and check-out dates
        selectedCheckInDate = null
        selectedCheckOutDate = null
        document.getElementById('id_check_in_date').value = ''
        document.getElementById('id_check_out_date').value = ''
        $('#id_reservation_time').prop('selectedIndex', 0);
        $('#id_reservation_time').prop('disabled', true);

        // Remove the "Check-in" and "Check-out" events from the calendar
        const checkInEvent = calendar.getEvents().find((event) => event.title === 'Check-in')
        if (checkInEvent) {
            checkInEvent.remove()
        }
        const checkOutEvent = calendar.getEvents().find((event) => event.title === 'Check-out')
        if (checkOutEvent) {
            checkOutEvent.remove()
        }

        // Disable the Clear button
        clearCheckInButton.style.display = 'none'
    })

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth', // Change the view as needed
        selectable: true, // Enable date selection
    
        select: function (info) {
            var selectedDate = new Date(info.startStr)
    
            // Check if the selected date is in the past
            if (selectedDate < new Date() && !isToday(info.startStr)) {
                alert("You can't select past dates.")
                calendar.unselect()
                return
            }
    
            // Check if the selected check-in date is after the check-out date
            if (selectedCheckOutDate && selectedDate > new Date(selectedCheckOutDate)) {
                alert('Check-in date cannot be after the check-out date.')
                calendar.unselect()
                return
            }
    
            // Handle date selection
            if (!selectedCheckInDate) {
                // Handle the click event for the "Clear" button
                const clearCheckInButton = document.getElementById('clearCheckIn')
                clearCheckInButton.addEventListener('click', function () {
                    // Clear the check-in date
                    selectedCheckInDate = null
                    document.getElementById('id_check_in_date').value = ''
    
                    // Remove the "Check-in" event from the calendar
                    const checkInEvent = calendar.getEventById('checkInEvent')
                    if (checkInEvent) {
                        checkInEvent.remove()
                    }
                })
    
                // Set the check-in date if it's not already set
                selectedCheckInDate = info.startStr
    
                document.getElementById('id_check_in_date').value = selectedCheckInDate
    
                // Add a "Check-in" event on the selected date
                calendar.addEvent({
                    title: 'Check-in',
                    start: selectedCheckInDate,
                    color: 'blue' // Customize the color for check-in date
                })
    
                // Show the "Clear" button when setting the check-in date
                document.getElementById('clearCheckIn').style.display = 'inline-block'
                $('#id_reservation_time').prop('disabled', false);
            }
            renderSelection()
        },
    
        selectAllow: function (selectInfo) {
            const selectedDate = selectInfo.start.toISOString().split('T')[0];
            
            // Get all events on the selected date
            const eventsOnSelectedDate = calendar.getEvents().filter(event => {
                const eventDate = event.start.toISOString().split('T')[0];
                return eventDate === selectedDate;
            });
        
            const isPool1Unavailable = eventsOnSelectedDate.some(event => event.backgroundColor && event.backgroundColor.includes('red'));
            const isPool2Unavailable = eventsOnSelectedDate.some(event => event.backgroundColor && event.backgroundColor.includes('yellow'));
        
            // Allow selection if either pool 1 or pool 2 is available
            return !isPool1Unavailable || !isPool2Unavailable;
        },
        
    
        events: unavailableEvents,
    
        selectOverlap: function (event) {
            // Check if both pool 1 (red) and pool 2 (yellow) are present in the background color
            const isPool1Unavailable = event.backgroundColor && event.backgroundColor.includes('red');
            const isPool2Unavailable = event.backgroundColor && event.backgroundColor.includes('yellow');
    
            // Prevent selection overlap only when both pool 1 and pool 2 are present
            return !event.backgroundColor || !(isPool1Unavailable && isPool2Unavailable);
        }
    });
    
    function renderSelection() {
        // Clear existing selections
        calendar.removeAllEventSources()
    
        // Add unavailable dates as events
        calendar.addEventSource({
            events: unavailableEvents,
            rendering: 'background'
        })
    
        // Add selected check-in and check-out dates as events
        if (selectedCheckInDate && selectedCheckOutDate) {
            calendar.addEvent({
                title: 'Check-out',
                start: selectedCheckOutDate,
                color: 'blue' // Customize the color for check-out date
            })
            var currentDate = new Date(selectedCheckInDate)
        }
    }
    
    calendar.render();
    
    // Your JavaScript code here to control form navigation and validation
    let currentStep = 0

    function updateStepVisibility() {
        steps.forEach((step, index) => {
            if (index === currentStep) {
                step.classList.remove('hidden')
            } else {
                step.classList.add('hidden')
            }
        })

        const translateX = -currentStep * 100 // 100% for each step
        prevStepButton.disabled = currentStep === 0
        submitReservationButton.style.display = currentStep === steps.length - 1 ? 'block' : 'none'

        // Show Step 2 fields when transitioning to Step 2
        if (currentStep === 1) {
            document.getElementById('step2').classList.remove('hidden')
        } else {
            document.getElementById('step2').classList.add('hidden')
        }

        // Enable or disable the "Next" button based on form validation
        if (currentStep < steps.length - 1) {
            nextStepButton.disabled = !isCurrentStepValid()
        } else {
            nextStepButton.disabled = true
        }
        // Show/hide buttons based on the current step
        if (currentStep === 0) {
            prevStepButton.style.display = 'none' // Hide "Previous" on the first step
        } else {
            prevStepButton.style.display = 'block' // Show "Previous" on other steps
        }

        if (currentStep === steps.length - 1) {
            nextStepButton.style.display = 'none' // Hide "Next" on the last step
            submitReservationButton.style.display = 'block' // Show "Submit Reservation" on the last step
        } else {
            nextStepButton.style.display = 'block' // Show "Next" on other steps
            submitReservationButton.style.display = 'none' // Hide "Submit Reservation" on other steps
        }
    }

    function isCurrentStepValid() {
        // Implement validation logic for each step
        if (currentStep === 0) {
            // Check if fields in Step 1 are filled
            // const numGuests = document.getElementById('id_num_guests').value
            const name = document.getElementById('id_guest_name').value
            const checkIn = document.getElementById('id_check_in_date').value
            const checkOut = document.getElementById('id_check_out_date').value
            return name !== '' && checkIn !== '' && checkOut !== ''
        } else if (currentStep === 1) {
            // Check if fields in Step 2 are filled
            const email = document.getElementById('id_guest_email').value
            const phone = document.getElementById('id_guest_phone').value
            return email !== '' && phone !== ''
        }
        // Add more validation for other steps if needed
        return true
    }

    prevStepButton.addEventListener('click', () => {
        if (currentStep > 0) {
            currentStep--
            updateStepVisibility()
        }
    })

    nextStepButton.addEventListener('click', () => {
        if (currentStep < steps.length - 1 && isCurrentStepValid()) {
            currentStep++
            updateStepVisibility()
        }
    })

    function isFormValid() {
        const currentStepFields = steps[currentStep].querySelectorAll('input[required], textarea[required]')
        for (const field of currentStepFields) {
            if (!field.value.trim()) {
                return false
            }
        }
        return true
    }

    // Update button states based on form validity
    function updateButtonState() {
        const currentStepFields = steps[currentStep].querySelectorAll('input[required], textarea[required]')
        for (const field of currentStepFields) {
            if (!field.value.trim()) {
                nextStepButton.disabled = true
                return // Exit the loop if any required field is empty
            }
        }
        nextStepButton.disabled = false // Enable the button if all required fields are filled
    }

    // Listen for input changes on all input fields and textareas within each step
    steps.forEach((step) => {
        const inputFields = step.querySelectorAll('input[required], textarea[required]')
        inputFields.forEach((field) => {
            field.addEventListener('input', updateButtonState)
        })
    })
    // Listen for input changes on the current step
    steps[currentStep].addEventListener('input', updateButtonState)

    // Initial button state
    updateButtonState()

    // Example: To submit the form when the final step is completed
    submitReservationButton.addEventListener('click', (e) => {
        e.preventDefault()
        form.submit() // Trigger the form submission
    })

    // Initial visibility setup
    updateStepVisibility()
})

function formatDate(date) {
    const year = date.getFullYear()
    const month = String(date.getMonth() + 1).padStart(2, '0')
    const day = String(date.getDate()).padStart(2, '0')
    return `${year}-${month}-${day}`
}

$(document).ready(function () {
    $('#id_discount_code').on('blur', function () {
        const discountCode = $(this).val()
        if (discountCode) {
            // Specify the URL for the "validate_discount_code" view
            const validateDiscountUrl = 'http://127.0.0.1:8000/validate_discount_code/'

            $.get(validateDiscountUrl, { discount_code: discountCode }, function (data) {
                if (data.valid) {
                    $('#discount-code-validation-message').text(`Discount code is valid (₱${data.discount_price})`)
                } else {
                    $('#discount-code-validation-message').text('Invalid discount code')
                }
            })
        }
    })
})