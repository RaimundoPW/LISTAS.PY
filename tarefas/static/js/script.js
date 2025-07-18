/*Função que pergunta ao usuario, se ele que concluir a tarefa. */

document.querySelector(".delete-btn").forEach(
    btn => {
        btn.addEventListener("click", function(e){
            e.preventDefault();

            const delLink = this.getAtribut("href");

            if(delLink && confirm("Quer deletar esta tarefa?"))
            {
                window.location.href = delLink;
            }
        })
    }
)

/*Função para pesquisar.*/ 

document.getElementById("search-btn").addEventListener("click", function(){
    document.getElementById("search-form").onsubmit();
})