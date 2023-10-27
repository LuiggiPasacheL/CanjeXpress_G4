<template>
  <img class="logo" src="../assets/logo.png" alt="Logo de CanjeXpress" />
  <h1>Registro</h1>

  <div class="register">
    <input type="text" v-model="name" placeholder="Ingresa tu nombre" />
    <input type="text" v-model="email" placeholder="Ingresa tu correo" />
    <input type="text" v-model="password" placeholder="Ingresa tu contraseña" />
    <button v-on:click="signUp">Registrarse</button>
    <p>
      <router-link to="/login">Ya tengo una cuenta</router-link>
    </p>
  </div>
</template>

<script>
export default {
  name: 'SignUp',
  data() {
    return {
      name: '',
      email: '',
      password: ''
    }
  },
  methods: {
    signUp() {
      console.log('signUp')
    }
  }
}
</script>

<style>
.register input {
  width: 200px;
  height: 25px;
  padding-left: 10px;
  display: block;
  margin-bottom: 10px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid #2c3e50;
}
.register button {
  width: 100px;
  height: 22px;
  border: 1px solid #2c3e50;
  background: #567799;
  color: white;
  cursor: pointer;
}
</style>
