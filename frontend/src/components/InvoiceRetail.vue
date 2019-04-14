<template>
  <div class="data-invoice container">
    <b-table :data="invoice" :columns="columns" v-if="invoice"></b-table>
  </div>
</template>

<script>
import { HTTP } from "@/plugins/axios";

export default {
  name: "invoice",
  data() {
    return {
      invoice: null,
      columns: [
        {
          field: "name",
          label: "Nom de l'article",
        },
        {
          field: "price",
          label: "prix"
        },
        {
          field: "quantity",
          label: "Quantité"
        }
      ]
    };
  },
  created() {
          this.id = this.$route.params.id;
      },
  async mounted() {
    try {
      this.invoice = await HTTP.get("/users/invoice/"+ this.id).then(response => {
        return response.data;
      });
    } catch (error) {
      console.error(error);
    }
  }
};
</script>

<style scoped>
.data-invoice {
  margin-top:80px;
}
</style>
