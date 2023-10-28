<template>
  <div class="container">
    <div class="row pt-5">
      <div class="col-md-1"></div>

      <div class="col-md-4 col-12">
        <img :src="product.imageURL" :alt="product.name" class="img-fluid" />
      </div>

      <div class="col-md-6 col-12 pt-3 pt-md-0">
        <h4>{{ product.name }}</h4>
        <h6 class="category font-italic">Categoria</h6>
        <h6 class="font-weight-bold">{{ product.points }} puntos</h6>

        <p><span class="font-weight-bold">Descripcion </span> <br />{{ product.description }}</p>

        <div class="d-flex flex-row justify-content-between">
          <div class="input-group col-md-3 col-4 p-0">
            <div class="input-group-prepend">
              <span class="input-group-text" id="basic-addon1">Cantidad</span>
            </div>
            <input class="form-control" type="number" v-model="quantity" />
          </div>

          <button id="wishlist-button" class="btn mr-3 p-1 py-0" style="background-color: #b3a594">
            Añadir a deseados
          </button>

          <button type="button" id="add-to-cart-button" class="btn">
            Canjear
            <ion-icon name="cart-outline" v-pre></ion-icon>
          </button>
        </div>

        <div class="features pt-3">
          <h5><strong>Detalles</strong></h5>
          <ul>
            <li>Lorem ipsum dolor sit amet consectetur adipisicing elit.</li>
            <li>Officia quas, officiis eius magni error magnam voluptatem</li>
            <li>nesciunt quod! Earum voluptatibus quaerat dolorem doloribus</li>
            <li>molestias ipsum ab, ipsa consectetur laboriosam soluta et</li>
            <li>ut doloremque dolore corrupti, architecto iusto beatae.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      product: {},
      id: null,
      quantity: 1
    }
  },
  props: ['API_URL', 'products'],
  mounted() {
    this.id = this.$route.params.id
    this.product = this.products.find((product) => product.id == this.id)
  }
}
</script>

<style>
.category {
  font-weight: 400;
}

/* Chrome, Safari, Edge, Opera navs */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

#add-to-cart-button {
  background-color: #febd69;
}
</style>
