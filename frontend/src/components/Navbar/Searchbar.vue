<template>
  <b-field class="search-bar">
    <b-input
      v-model="query"
      placeholder="Search..."
      @keydown.native.enter="submit"
      expanded
    >
    </b-input>
    <p class="control" @click="submit">
      <button class="button is-primary">
        <b-icon icon="search" size="is-small"></b-icon>
      </button>
    </p>
  </b-field>
</template>

<script>
export default {
  data() {
    return {
      query: ""
    };
  },
  methods: {
    submit() {
      if (this.query !== undefined && this.query.trim() !== "") {
        const formattedQuery = this.query.trim();
        this.$router.push({
          name: "Catalog",
          query: {
            search: formattedQuery
          }
        });
      }
    }
  }
};
</script>

<style lang="sass" scoped>
.search-bar
  margin-bottom: unset !important;
  width: 50%;
</style>
