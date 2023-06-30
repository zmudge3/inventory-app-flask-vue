<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h2>{{ name }}: Items</h2>
        <br>
        <button
          type="button"
          class="btn btn-success"
          @click="handleNewButton">
          New Item
        </button>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in items" :key="index">
              <td>{{ item.name }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-primary btn-sm">View</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      items: [],
      containerID: null
    };
  },
  methods: {
    getItems() {
      const path = `http://localhost:5001/${this.containerID}`;
      axios.get(path)
        .then((res) => {
          this.name = res.data.name;
          this.items = res.data.items;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.containerID = this.$route.params.containerID;
    this.getItems();
  },
};
</script>
