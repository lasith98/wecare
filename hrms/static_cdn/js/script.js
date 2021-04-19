
function change(id) {
    var nurse_obj = document.getElementById(id)

    var tag =  nurse_obj.getAttribute( 'data-true')

    if (tag == 'true') {

        nurse_obj.getElementsByClassName('left').item(0).classList.add('display-none')
        nurse_obj.getElementsByClassName('right').item(0).classList.remove('display-none')

        nurse_obj.setAttribute('data-true' , 'false')

        nurse_obj.getElementsByClassName('alocateToggle').item(0).setAttribute('name' , 'allocated')

        nurse_obj.remove()
        var alocated = document.getElementById('allocated')
        alocated.innerHTML += nurse_obj.outerHTML

    }else if(tag == 'false'){
        nurse_obj.getElementsByClassName('right').item(0).classList.add('display-none')
        nurse_obj.getElementsByClassName('left').item(0).classList.remove('display-none')

        nurse_obj.setAttribute('data-true' , 'true')
        nurse_obj.getElementsByClassName('alocateToggle').item(0).setAttribute('name' , 'unAllocated')


        nurse_obj.remove()
        var alocated = document.getElementById('unAllocated')
        alocated.innerHTML += nurse_obj.outerHTML
    }

}

function download(){
    var nowDate = new Date();
    var date = nowDate.getFullYear()+'/'+(nowDate.getMonth()+1)+'/'+nowDate.getDate();
    saveAsExcel('print_table_shift', date+' shift.xls')
}