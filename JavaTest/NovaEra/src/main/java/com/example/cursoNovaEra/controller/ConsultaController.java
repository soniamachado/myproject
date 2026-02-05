package com.example.cursoNovaEra.controller;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import com.example.cursoNovaEra.domain.CepDomain;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
//@ (anotar) o Restcontroler e autorizações dessas alterações com Mapear as aquisições
@RestController
@RequestMapping("api/cep")
public class ConsultaController {
  //Requisição do tipo GET para recuperar dados do servidor;@é anotation 
  // httpps://localhost:8081/consultaCep/{cep}
  @GetMapping ("/{cep}")
  public CepDomain consultaCep(@PathVariable("cep") String cep) {
    RestTemplate restTemplate = new RestTemplate();//restTemplate é uma classe que faz a requisição HTTP para a API do VIACEP(uma API externa)
    //response sent:dar uma respota costumizada para as aquisições que são feitas pelo nosso servidor , %s é indicar que o cep é uma variável
    String url = String.format("https://viacep.com.br/ws/%s/json/", cep);
    ResponseEntity<CepDomain> response=restTemplate.getForEntity(url,CepDomain.class);
  return response.getBody();
  } //response sent:dar uma respota costumizada para as aquisições que são feitas pelo nosso servidor 
}
