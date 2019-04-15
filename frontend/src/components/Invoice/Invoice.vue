<template>
  <div v-if="invoice && username" class="data-invoice container">
    <p class="user">All invoice for {{ username.username }}</p>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Amount</th>
          <th scope="col">Date</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, idx) in invoice" :key="idx">
          <td scope="col">
            <router-link
              :to="{ name: 'InvoiceRetail', params: { id: item.id_invoice } }"
              ><strong>{{ item.id_invoice }}</strong></router-link
            >
          </td>
          <td scope="col">${{ item.montant }}</td>
          <td scope="col">{{ item.transaction_date }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { HTTP } from "@/plugins/axios";

export default {
  name: "invoice",
  data() {
    return {
      username: null,
      invoice: null
    };
  },
  created() {
    //this.id = this.$route.params.id;
    this.id = 1;
  },
  async mounted() {
    try {
      this.invoice = await HTTP.get("/users/" + this.id + "/invoices").then(
        response => {
          return response.data;
        }
      );
      this.username = await HTTP.get("/users/" + this.id).then(response => {
        return response.data;
      });
    } catch (error) {
      console.error(error);
    }
  }
};
</script>

<style scoped>
table {
  width: 100%;
  box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1), 0 0 0 1px rgba(10, 10, 10, 0.1);
}
.user {
  margin-bottom: 20px;
}

.data-invoice {
  margin-top: 60px;
  background-color: #f5f5f5;
  padding: 20px;
}
</style>
