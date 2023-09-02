var break=[5,5,15]
var con=true;
function add()
{
    while(con)
    {
        var ad=prompt("Add a break time:");
        break.push(ad);
        var c=prompt("Do you wanne continue{Y/N}");
        if(c=='y' && a=='Y')
        con=true;
    }
    add()
}