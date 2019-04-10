<template>
  <aside class="column is-one-fifth">
    <p class="subtitle is-4">
      {{ department }}
    </p>
    <br />
    <p class="menu-label">
      Filter
    </p>
    <ul class="menu-list">
      <b-dropdown aria-role="list">
        <button class="button is-primary" slot="trigger">
          <span>Per page</span>
          <b-icon icon="caret-down"></b-icon>
        </button>
        <b-dropdown-item aria-role="listitem" @click="updatePerPage(10)"
          >10</b-dropdown-item
        >
        <b-dropdown-item aria-role="listitem" @click="updatePerPage(50)"
          >50</b-dropdown-item
        >
        <b-dropdown-item aria-role="listitem" @click="updatePerPage(100)"
          >100</b-dropdown-item
        >
      </b-dropdown>
    </ul>
    <p class="menu-label">
      Avg. Customer Review
    </p>
    <ul class="menu-list">
      <li @click="updateRating(4)">
        <a>
          <star-rating
            :rating="4"
            read-only
            :show-rating="false"
            :star-size="20"
          />
        </a>
      </li>
      <li @click="updateRating(3)">
        <a>
          <star-rating
            :rating="3"
            read-only
            :show-rating="false"
            :star-size="20"
          />
        </a>
      </li>
      <li @click="updateRating(2)">
        <a>
          <star-rating
            :rating="2"
            read-only
            :show-rating="false"
            :star-size="20"
          />
        </a>
      </li>
      <li @click="updateRating(1)">
        <a>
          <star-rating
            :rating="1"
            read-only
            :show-rating="false"
            :star-size="20"
          />
        </a>
      </li>
    </ul>
  </aside>
</template>

<script lang="ts">
export default {
  props: {
    department: String
  },
  methods: {
    updatePerPage(value) {
      this.$emit("update:perPage", value);
    },
    updateRating(value) {
      this.$emit("update:rating", value);
    }
  }
};
</script>

<style scoped>
.menu {
  width: 50%;
}
</style>
