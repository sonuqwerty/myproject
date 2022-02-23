function validateform()
{
    x = document.forms["myform"]["email"].value;
    if (x == "")
    {
        document.getElementById('email').placeholder = "Enter your email";
        document.getElementById('email').style.border = "2px solid red";
        document.getElementById('valid').innerHTML = "Enter Your email";
        var x = document.getElementById("valid");
        x.innerHTML = "Enter your eamil";
        x.style.color = "red";
        return false;
    }
}

function crElement()
{
 // x = document.getElementByClassName("myname");
  //console.log(x);
  //x[0].innerHTML = "hii";
  x = document.createElement("input");
  z = document.createElement("label");
 // x.setAttribute("class","myname");
 // y = document.getElementById("mydiv");
 // y.appendChild(x);
 // y.appendChild(z);
}
