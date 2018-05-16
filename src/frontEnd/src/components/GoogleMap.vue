<template>
  <div>
    <br>
    <gmap-map
      :center="center"
      :zoom="15"
      style="width:100%;  height: 200px;"
    >
      <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        @click="center=m.position"
      ></gmap-marker>
    </gmap-map>
  </div>
</template>

<script>
const marker = {
  lat: 48.8156781,
  lng: 2.3628608000000213
}
export default {
  name: 'GoogleMap',
  data () {
    return {
      center: {lat: 48.8156781, lng: 2.3628608000000213},
      markers: [marker],
      places: [],
      currentPlace: null
    }
  }
}
</script>
