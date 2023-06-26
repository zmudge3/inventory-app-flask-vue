<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Containers</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col"># Items</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(container, index) in containers" :key="index">
              <td>{{ container.name }}</td>
              <td>{{ container.items.length }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-success btn-sm">View</button>
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
      containers: [],
    };
  },
  methods: {
    getContainers() {
      const path = 'http://localhost:5001/containers';
      axios.get(path)
        .then((res) => {
          this.containers = res.data.containers;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getContainers();
  },
};
</script>
