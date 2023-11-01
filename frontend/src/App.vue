<template>
  <Navbar />
  <router-view style="min-height: 60vh" :API_URL="API_URL">
  </router-view>
  <Footer />
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  data() {
    return {
      API_URL: import.meta.env.VITE_API_URL,
      products: null
    }
  },

  components: {
    Navbar,
    Footer
  },

  methods: {
    async fetchData() {
      fetch(`${this.API_URL}/products/`)
        .then((res) => res.json())
        .then((json) => {
          this.products = json
        })
        .catch((err) => {
          console.error('Error al cargar los datos: ', err)
        })
    }
  },
  mounted() {
    this.fetchData()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body {
  padding: 0;
  margin: 0;
}
.logo {
  width: 100px;
}
</style>
