<template>
  <div class="data-invoice container">
    <p> All invoice for  {{username.username}} </p>


    <template>
        <div class="table-responsive">
            <table class="table-hover" v-if="invoice">
                <thead>
                    <tr>
                        <th>Id invoice</th>
                        <th>Amount $</th>
                        <th>Date </th>

                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(item, idx) in invoice">
                        <router-link :to="{ name: 'InvoiceRetail', params: { id: item.id_invoice }}">item.id_invoice</router-link>
                        <td>{{ item.montant }}</td>
                        <td>{{ item.transaction_date}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </template>


      <!--  <b-table :data="invoice" :columns="columns" v-if="invoice"></b-table> -->


  </div>
</template>

<script>
import { HTTP } from "@/plugins/axios";

export default {
  name: "invoice",
  data() {
    return {
      username: null,
      invoice: null,
      columns: [
        {
          field: "id_invoice",
          label: "ID invoice",
        },
        {
          field: "montant",
          label: "Somme total $"
        },
        {
          field: "transaction_date",
          label: "Date"
        }
      ]
    };
  },
  created() {
          //this.id = this.$route.params.id;
          this.id = 1
      },
  async mounted() {
    try {
      this.invoice = await HTTP.get("/users/"+ this.id + "/invoices").then(response => {
        return response.data;
      });
      this.username = await HTTP.get("/users/"+ this.id).then(response => {
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
  margin-top:60px;
}
</style>
