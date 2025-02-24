<template>
    <div class="container">
      <div class="card">
        <div class="card-header">
          Cursos
        </div>
        <div class="card-body">
          <table class="table">
            <thead>
              <tr>
                <th>Seleccionar</th>
                <th>Código</th>
                <th>Curso</th>
                <th>Docente</th>
                <th>Horario</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(curso, index) in cursos" :key="curso.codigo">
                <td>
                  <!-- Checkbox para seleccionar el curso -->
                  <div class="d-flex flex-column align-items-center">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      :id="'check-' + index"
                      :value="curso.codigo"
                      v-model="selectedCursos"
                    />
                    <label :for="'check-' + index"></label>
                  </div>
                </td>
                <td>{{ curso.codigo }}</td>
                <td>{{ curso.curso }}</td>
                <td>{{ curso.docente }}</td>
                <td>{{ curso.horario }}</td>
              </tr>
            </tbody>
          </table>
  
          <!-- Botón de Confirmar Matrícula -->
          <div class="d-flex justify-content-center mt-4">
            <button class="btn btn-success" @click="confirmarMatricula">
              Confirmar Matrícula
            </button>
          </div>
  
          <!-- Mensaje de error -->
          <div v-if="errorMessage" class="alert alert-danger mt-3">
            {{ errorMessage }}
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        cursos: [],
        selectedCursos: [], // Aquí se almacenarán los códigos de los cursos seleccionados
        errorMessage: ''    // Mensaje de error que se muestra si hay conflicto de horarios
      }
    },
    created() {
      this.consultarcursos();
    },
    methods: {
      consultarcursos() {
        fetch('http://localhost:8000/api.php')
          .then(respuesta => respuesta.json())
          .then(datosderespuesta => {
            console.log(datosderespuesta);
            // Asignamos los datos a la variable 'cursos'
            this.cursos = typeof datosderespuesta[0].success === 'undefined'
              ? datosderespuesta
              : [];
          })
          .catch(console.log);
      },
      confirmarMatricula() {
        // Enviar los códigos seleccionados al endpoint de Flask
        fetch('http://localhost:5000/confirmar_matricula', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ cursos_seleccionados: this.selectedCursos })
        })
        .then(res => res.json())
        .then(data => {
          if (data.error) {
            // Si hay error (por ejemplo, horario incompatible), se muestra en la página
            this.errorMessage = data.mensaje || data.error;
          } else {
            this.errorMessage = '';
            alert(data.mensaje);
            // Aquí puedes realizar otras acciones, como limpiar la selección o redirigir.
          }
        })
        .catch(error => {
          console.error(error);
          this.errorMessage = 'Error en la comunicación con el servidor';
        });
      }
    }
  }
  </script>
  