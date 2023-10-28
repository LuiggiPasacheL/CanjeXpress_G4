<template>
  <div class="card h-100 w-100">
    <div class="embed-responsive embed-responsive-16by9">
      <img
        class="card-img-top embed-responsive-item"
        :src="product.imageURL"
        alt="Card image cap"
      />
    </div>
    <div class="card-body">
      <router-link :to="{ name: 'Product-details-page', params: { id: product.id } }">
        <h5 class="card-title">{{ product.name }}</h5>
      </router-link>
      <p class="card-text">{{ product.description.substring(0, 60) }}...</p>
      <p class="card-text">{{ product.points }} puntos</p>
      <a href="#" class="btn btn-primary">Canjear</a>
    </div>
  </div>
</template>
<script>
export default {
  name: 'ProductBox',
  props: ['product']
}
</script>
<style scoped>
.card-img-top {
  object-fit: cover;
}
</style>
