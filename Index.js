var myCookies = {};

function saveCookies()
{
    myCookies["_phone"] = document.getElementById("phone").value;
    myCookies["_email"] = document.getElementById("email").value;
    myCookies["_min"] = document.getElementById("min").value;
    myCookies["_drop"] = document.getElementById("drop").value;
    myCookies["_slideo"] = document.getElementById("slidero").value;
    myCookies["_slidet"] = document.getElementById("slidert").value;
    //Start reuseable code
    document.cookie = "";
    var expiresAttrib = new Date(Date.now()+60*1000).toString();
    var cookieString = "";
    for (var key in myCookies)
    {
        cookieString = key+"="+myCookies[key]+";"+expiresAttrib+";";
        document.cookie = cookieString;
    }
    //End reuseable code
    document.getElementById("out").innerHTML = doccument.cookie;
}
function loadCookies()
{
    //start reuseable code
    myCookies = {};
    var kv = document.cookie.split(";");
    for (var id in kv)
    {
        var cookie = kv[id].split("=");
        myCookies[cookie[0].trim()] = cookie[1];
    }
    //end reuseable code
    document.getElementById("phone").value = myCookies["_phone"];
    document.getElementById("email").value = myCookies["_email"];
    document.getElementById("min").value = myCookies["_min"];
    document.getElementById("drop").value = myCookies["_drop"];
    document.getElementById("slidero").value = myCookies["_slideo"];
    document.getElementById("slidert").value = myCookies["_slidet"];
}