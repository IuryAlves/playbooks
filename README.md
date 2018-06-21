* [Requisitos](#requisitos)
* [Instalação](#instalacao)
* [Rodando um playbook](#rodando-um-playbook)
* [Ambiente de Testes](#ambiente-de-testes)
    * [Acessando o Vagrant via ssh](#acessando-o-vagrant-via-ssh)
    * [Rodando um playbook dentro do vagrant](#rodando-um-playbook-dentro-do-vagrant)

<a name='requisitos'></a>
## Requisitos

*    Python
*    pip
*    virtualenv
*    virtualenvwrapper
*    Vagrant
*    VirtualBox

<a name='instalacao'></a>
## Instalação

* crie um virtualenv:

```
mkvirtualenv playbooks --python=$(which python2)
```

* Instale as dependências

```
pip install -r requirements.txt
```


<a name='rodando-um-playbook'></a>
## Rodando um playbook

```
ansible-playbook ansible/plays/<play>/main.yml
```

Onde `<play>` é o nome do seu playbook

 
<a name='ambiente_de_testes'></a>
## Ambiente de Testes

Usamos o Vagrant para criar uma máquina de teste para os playbooks.


Para subir um Vagrant faça:

```
vagrant up
```


#### Acessando o Vagrant via ssh

```
vagrant ssh
```


#### Rodando um playbook dentro do vagrant


```
ansible-playbook <playbook-name> -i local.hosts testserver
``


