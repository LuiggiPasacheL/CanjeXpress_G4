<template>
  <img class="logo" src="../assets/logo.png" alt="Logo de CanjeXpress" />
  <h1>Iniciar Sesión</h1>

  <div class="login">
    <input type="text" v-model="email" placeholder="Ingresa tu correo" />
    <input type="text" v-model="password" placeholder="Ingresa tu contraseña" />
    <button v-on:click="login">Acceder</button>
    <p>
      <router-link to="/sign-up">Aun no tengo una cuenta</router-link>
    </p>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    login() {
      console.log(result)
    }
  }
}
</script>

<style>
.login input {
  width: 200px;
  height: 25px;
  padding-left: 10px;
  display: block;
  margin-bottom: 10px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid #2c3e50;
}
.login button {
  width: 100px;
  height: 22px;
  border: 1px solid #2c3e50;
  background: #567799;
  color: white;
  cursor: pointer;
}
</style>
