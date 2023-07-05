<template>
  <div class="container">
    <itemForm
      :containerID=containerID
      v-if="showItemForm"
      @showItemForm="showItemForm = $event"
      @showContainerItems="showContainerItems = $event">
    </itemForm>
  </div>
  <div class="container" v-if="showContainerItems && loaded">
    <button
      type="button"
      class="btn btn-outline-primary"
      @click="handleBackButton">
      <i class="fa-solid fa-arrow-left"></i> Back
    </button>
    <br><br>
    <div class="row">
      <div class="col-sm-10">
        <h2>{{ name }}: Items</h2>
        <br>
        <alert :message=message v-if="showMessage"></alert>
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
              <th scope="col">Quantity</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in items">
              <td>{{ item.name }}</td>
              <td>{{ item.quantity }}</td>
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
import ItemForm from './ItemForm.vue';

export default {
  data() {
    return {
      name: '',
      items: [],
      containerID: null,
      showContainerItems: true,
      showItemForm: false,
      message: '',
      showMessage: false,
      loaded: false,
    };
  },
  components: {
    alert: Alert,
    itemForm: ItemForm,
  },
  methods: {
    getItems() {
      const path = `http://localhost:5001/containers/${this.containerID}`;
      axios.get(path)
        .then((res) => {
          this.name = res.data.name;
          this.items = res.data.items;
          this.loaded = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleNewButton() {
      this.showItemForm = true;
      this.showContainerItems = false;
    },
    handleMessage(message) {
      this.showMessage = true;
      this.message = message;
      setTimeout(() => {
        this.showMessage = false;
      }, 5000);
    },
    handleBackButton() {
      this.$router.go(-1);
    },
  },
  created() {
    this.containerID = this.$route.params.containerID;
    this.getItems();
  },
};
</script>
