const urlParams = new URLSearchParams(window.location.search);
const erro = urlParams.get('erro');

document.querySelector("body > div.main > div.login > form > label").click()

if(erro == '0'){

	let erromsg = 'usuario não registrado no sistema.'
	document.querySelector('.erro').textContent = erromsg
	document.querySelector("label").click()
} 


else if(erro == '1'){

	let erromsg = 'a senha está incorreta.'
	document.querySelector('.erro').textContent = erromsg
}

else if (erro == '2'){

	let erromsg = 'email já esta cadastrado, se esqueceu a senha entre em contato.'
	document.querySelector('.erro').textContent = erromsg
}

else if (erro == '3'){

	let erromsg = 'usuario cadastrado com sucesso, faça login novamente!'
	document.querySelector('.erro').textContent = erromsg
	document.querySelector('.erro').style.color = 'green'

}

else if (erro == '4'){

	let erromsg = 'sua sessão expirou, faça login novamente.'
	document.querySelector('.erro').textContent = erromsg

}