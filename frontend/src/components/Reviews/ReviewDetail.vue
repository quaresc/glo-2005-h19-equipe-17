<template>
  <div class="column is-full">
    <div class="card is-fullheight">
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <p class="title is-6">{{ review.title }}</p>
            <p class="subtitle is-6">By {{ review.username }}</p>
            <p class="subtitle is-6">{{ review.comment }}</p>
            <star-rating :rating="review.rating" read-only :show-rating="false" :star-size="20"/>
            <p class="subtitle is-6">{{ review.timestamp }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    review: Object
  }
};
</script>

<style lang="sass" scoped>
img
  object-fit: contain;
  cursor: pointer;
.card
  display: flex
  flex-direction: column
  &.is-fullheight
    height: 100%;
.card-footer
  margin-top: auto;
</style>