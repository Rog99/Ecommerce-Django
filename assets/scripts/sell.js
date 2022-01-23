function display_tags(){
    let type = document.getElementById("products").value;
    let tags = document.getElementById("book_tags");
    if(type == "BK"){
        tags.styles.visibility = "hidden";
    }
    else{
        tags.styles.visibility = "initial";
    }
}