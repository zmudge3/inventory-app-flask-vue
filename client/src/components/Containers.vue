<template>
  <div class="container">
    <containerForm
      v-if="showContainerForm"
      @showContainerForm="showContainerForm = $event"
      @showContainerList="showContainerList = $event">
    </containerForm>
  </div>
  <div class="container" v-if="showContainerList && loaded">
    <div class="row">
      <div class="col-sm-10">
        <h1>Containers</h1>
        <br>
        <alert :message=message v-if="showMessage"></alert>
        <button
          type="button"
          class="btn btn-success"
          @click="handleNewButton">
          New Container
        </button>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col"># Items</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="container in containers">
              <td>{{ container.name }}</td>
              <td>{{ container.items.length }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-primary btn-sm"
                    @click="handleViewButton(container.id)">
                    View
                </button>
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
import Alert from './Alert.vue';
import ContainerForm from './ContainerForm.vue';

export default {
  data() {
    return {
      containers: [],
      showContainerForm: false,
      showContainerList: true,
      message: '',
      showMessage: false,
      loaded: false,
    };
  },
  components: {
    alert: Alert,
    containerForm: ContainerForm,
  },
  methods: {
    getContainers() {
      const path = 'http://localhost:5001/containers';
      axios.get(path)
        .then((res) => {
          this.containers = res.data.containers;
          this.loaded = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleNewButton() {
      this.showContainerForm = true;
      this.showContainerList = false;
    },
    handleMessage(message) {
      this.showMessage = true;
      this.message = message;
      setTimeout(() => {
        this.showMessage = false;
      }, 5000);
    },
    handleViewButton(containerID) {
      this.$router.push({name: 'ContainerItems', params: {containerID: containerID}});
    },
  },
  created() {
    this.getContainers();
  },
};
</script>
