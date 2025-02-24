<template>
  <nav>
    <router-link to="/">Home</router-link> 

    
  </nav>
  <router-view/>
</template>

<style>

body {
  background: url('C:\Users\Tata\Documents\proyecto\gestor\images7.png') no-repeat center center fixed;
  background-size: cover;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
