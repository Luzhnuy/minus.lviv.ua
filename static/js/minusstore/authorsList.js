

let page = 2;
// let scroll;
let letter = document.getElementById('letter').textContent;
console.log(letter);
window.onscroll=() =>  {
    let scroll = window.scrollY;
    let ul_scroll = document.getElementById("authors").lastElementChild;
    console.log(ul_scroll.getBoundingClientRect().top);
    if (scroll > ul_scroll.getBoundingClientRect().top && scroll < ul_scroll.getBoundingClientRect().top+200) {
        if(letter ===''){
            letter = 'А';
        }
        fetch('http://127.0.0.1:8000/minusstore/get_authors/'+letter+'/?page=' + page).then(res => res.json()).then((result) => {


                for (let author of result){
                    $("#authors").append(
                        "<li class='authors_li'><div class='collapsible-header gaveminus' id='" +author.id + "'><a style='textDecoration: underline;'>"+author.name +"</a> <span class='badge'></span></div><div class='collapsible-body' style='display: none;\n" +
                        "border-bottom: 1px solid #ddd;\n" +
                        "-webkit-box-sizing: border-box;\n" +
                        "box-sizing: border-box;\n" +
                        "padding: 2rem;' id='"+author.id+'b' + "> </div> </li>"
                    );
                }

                


            });
        page++;


    }
};


