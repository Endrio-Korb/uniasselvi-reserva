


const chk_lab = document.getElementById('checkbox-field')

if (chk_lab) {
    const reservados = document.querySelector('#reservados')
    const disponiveis = document.querySelector('#disponiveis')
    chk_lab.addEventListener('change', () => {
        if (chk_lab.checked == true){
            reservados.classList.remove('destaque')
            disponiveis.classList.toggle('destaque')
        } else {
            disponiveis.classList.remove('destaque')
            reservados.classList.toggle('destaque')
        }
    })
}


function sidebar() {
    const chkSidebar = document.getElementById("chk-burguer")
    const sidebar = document.querySelector('.sidebar')
    chkSidebar.addEventListener('change', () => {
        if (chkSidebar.checked == true) {
            sidebar.classList.toggle('active')
        } else {
            sidebar.classList.remove('active')
        }
    })
}