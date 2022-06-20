function preventRefreshing() {
    // להביא את המידע מהעמוד שקיים
        const params = new URLSearchParams(window.location.search)
        for (const param of params) {
            console.log(param)
        }
        drive_id_var= document.getElementById("drive_id").value
        console.log("drive_id")
        console.log(drive_id_var)
        driver_id_var= document.getElementById("driver_id").value
        console.log("driver_id")
        console.log(driver_id_var)
        passenger_id_var= document.getElementById("passenger_id").value
        console.log("passenger_id")
        console.log(passenger_id_var)


             // מטפל ברענן שלא יעשה את זה שוב
    if (window.history.replaceState) {
        window.history.replaceState(null, null, window.location.href);
    }


}

    if (window.history.replaceState) {
        window.history.replaceState(null, null, window.location.href);
    }
