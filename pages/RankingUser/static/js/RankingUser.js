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
        console.log("i am here")
        window.history.replaceState(null, null, window.location.href);
    }

            //דרך 1 לא עבד בגלל הדולר
        //
        // const domain= "//127.3.3.7:5000"
        // const add_params= {
        //     drive_id: drive_id_var,
        //     driver_id: driver_id_var,
        // }
        // const new_params =new URLSearchParams([
        // ...Object.entries(add_params),
        // ]).toString();
        //
        // console.log("1")
        // console.log(new_params);
        //
        // const new_url = new URL("http://127.3.3.7:5000/RankingUser?${new_params}");
        //  console.log(new_url.href);

     //דרך 2 שולח לעמוד שלא נמצא
     //    const domain_2= "http://127.3.3.7:5000/RankingUser?"
     //    let searchParams = new URLSearchParams(domain_2);
     //    for (let p of searchParams) {
     //        console.log("qq");
     //        console.log(p);
     //    }
     //    searchParams.append('drive_id', drive_id_var);
     //    searchParams.append('driver_id', driver_id_var);
     //
     //    const a= searchParams;
     //    console.log("a");
     //     console.log(a);


}

    if (window.history.replaceState) {
        console.log("i am here 2")
        window.history.replaceState(null, null, window.location.href);
    }
