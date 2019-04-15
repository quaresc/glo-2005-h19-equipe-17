<template>
  <nav
    class="navbar is-fixed-top is-secondary"
    role="navigation"
    aria-label="main navigation"
  >
    <div class="navbar-brand">
      <a class="navbar-item">
        <router-link :to="{ name: 'Home' }">
          <div class="is-size-2-desktop is-size-2-touch">
            <p id="brand">WorstBuy</p>
          </div>
        </router-link>
      </a>

      <a
        role="button"
        class="navbar-burger burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div class="navbar-menu">
      <div class="navbar-start">
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            <strong>Departments</strong>
          </a>
          <div v-if="departments" class="navbar-dropdown">
            <div class="media">
              <div class="media-content">
                <a
                  class="navbar-item"
                  v-for="(department, index) in departments"
                  :key="index"
                  @click="redirect(department.name)"
                  >{{ department.name }}</a
                >
                <hr class="navbar-divider" />
                <a class="navbar-item" @click="redirect()">
                  Check all products
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <searchbar class="navbar-item"></searchbar>
      <div class="navbar-end">
        <div class="navbar-item">
          <router-link :to="{ name: 'Invoices' }">
            <button class="button is-secondary">
              <b-icon icon="file-invoice-dollar" size="is-small"> </b-icon>
              <strong>Invoices</strong>
            </button>
          </router-link>
          <router-link :to="{ name: 'Cart' }">
            <button class="button is-secondary">
              <b-icon icon="shopping-cart" size="is-small"> </b-icon>
              <strong>Cart</strong>
            </button>
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { HTTP } from "@/plugins/axios";
import Searchbar from "@/components/Navbar/Searchbar.vue";
export default {
  data() {
    return {
      departments: null
    };
  },
  components: {
    Searchbar
  },
  async mounted() {
    await this.getDepartements();
  },
  methods: {
    async getDepartements() {
      try {
        await HTTP.get("/departments/").then(response => {
          this.departments = response.data.departments;
        });
      } catch (error) {
        console.error(error);
      }
    },
    redirect(department) {
      if (department) {
        this.$router.push({
          name: "Catalog",
          params: { department: department }
        });
      } else {
        this.$router.push({
          name: "Catalog"
        });
      }
    }
  }
};
</script>

<style scoped>
[data-badge]::after {
  background: #ff9508 !important;
}
.navbar {
  height: 4.1rem;
}
.navbar-dropdown {
  max-height: 50vh;
  overflow-y: scroll;
}
#brand {
  font-family: "Alfa Slab One", cursive;
}
</style>
