<template>
  <div class="column is-one-fifth-desktop is-one-third-tablet">
    <div class="card is-fullheight">
      <div class="card-image">
        <figure class="image is-square">
          <img :src="product.image_url" />
        </figure>
      </div>
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <p class="title is-6">{{ product.name }}</p>
            <p class="subtitle is-6">{{ product.type }}</p>
          </div>
        </div>

        <div class="content">${{ product.price }}</div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    product: Object
  }
};
</script>

<style lang="sass" scoped>
img
  object-fit: contain;
  cursor: pointer;
.card 
  &.is-fullheight
    height: 100%;
</style>