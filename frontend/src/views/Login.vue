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
        <p :class="{ 'hidden': !isLogin }">
            inicio de sesión exitoso
        </p>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            email: '',
            password: '',
            isLogin: false
        }
    },
    methods: {
        async login() {
            const API_URL = import.meta.env.VITE_API_URL  + '/login'
            console.log(API_URL)
            try {
                const response = await fetch(API_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        username: this.email,
                        password: this.password,
                    }),
                });

                if (!response.ok) {
                    throw new Error('Inicio de sesión fallido');
                }

                const data = await response.json();
                // Procesa los datos de inicio de sesión o realiza las acciones necesarias aquí

                this.isLogin = data.success;

                console.log('Inicio de sesión exitoso', data);
            } catch (error) {
                console.error('Error al iniciar sesión:', error);
            }
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

.login .hidden {
    display: none;
}
</style>
