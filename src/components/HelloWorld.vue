<template>
  <div class="container">
    <button class="btn-iniciar" @click="irAListarCursos">Iniciar</button>
  </div>
</template>

<script>
export default {
  name: 'InicioMatricula',
  methods: {
    irAListarCursos() {
      this.$router.push('/listar');
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 30vh; /* Centrar en toda la pantalla */
}

.btn-iniciar {
  background-color: #41B883;
  color: white;
  font-size: 1.5rem;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-iniciar:hover {
  background-color: #369870;
}
</style>

