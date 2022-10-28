<script>
  export default {
    data() {
      return {
        livros: []
      }
    },
    mounted() {
        this.getAllDatas();
    },
    methods: {
      async getAllDatas() {
        try{
          const response = await fetch('/api/livros', {
            method: 'GET',
            headers: {'Content-Type': 'application/json'}
          }).then(e => e.json())
          this.livros = response;
        } catch (e){
          console.log("Falha na request");
        }
      }
    }
  }
</script>

<template>
  <main>
    <h1>Livros: </h1>
    <table>
      <thead>
        <tr>
          <th>Id</th>
          <th>Author</th>
          <th>Title</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="livro in livros" :key="livro.id">
          <td>{{livro.id}}</td>
          <td>{{livro.author}}</td>
          <td>{{livro.titulo}}</td>
        </tr>
      </tbody>
    </table>
      
  </main>
</template>

<style scoped>
  
</style>