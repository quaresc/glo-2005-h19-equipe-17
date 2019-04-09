<template>
  <aside
    class="menu is-2 is-narrow-mobile is-fullheight section is-hidden-mobile"
  >
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
      Price
    </p>
    <ul class="menu-list">
      <li><a>Under $10</a></li>
      <li><a>$10 to $25</a></li>
      <li><a>$25 to $50</a></li>
      <li><a>$50 and above</a></li>
    </ul>
    <p class="menu-label">
      Avg. Customer Review
    </p>
    <ul class="menu-list">
      <li>
        <star-rating
          :rating="4"
          read-only
          :show-rating="false"
          :star-size="20"
        />
      </li>
      <li>
        <star-rating
          :rating="3"
          read-only
          :show-rating="false"
          :star-size="20"
        />
      </li>
      <li>
        <star-rating
          :rating="2"
          read-only
          :show-rating="false"
          :star-size="20"
        />
      </li>
      <li>
        <star-rating
          :rating="1"
          read-only
          :show-rating="false"
          :star-size="20"
        />
      </li>
    </ul>
  </aside>
</template>

<script lang="ts">
export default {
  methods: {
    updatePerPage(value) {
      this.$emit("update:perPage", value);
    }
  }
};
</script>

<style scoped>
.menu {
  width: 50%;
}
</style>
