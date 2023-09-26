import { convertVietnamese, getNameFromId } from "./utils.js";
import useModelList from "./useModelList.js";

const { createApp, ref, onMounted, computed } = Vue;
const { createVuetify } = Vuetify;

const vuetify = createVuetify();
const app = createApp({
  setup() {
    const province = ref(null);
    const district = ref(null);
    const ward = ref(null);

    // Loading provinces
    const {
      isLoading: isLoadingProvinces,
      results: provinces,
      getResults: getProvinces,
    } = useModelList("provinces");

    onMounted(async () => {
      await getProvinces({ basic: true, limit: 100 });
    });

    // Loading districts when province get new value
    const {
      isLoading: isLoadingDistricts,
      results: districts,
      getResults: getDistricts,
    } = useModelList("districts");

    const onUpdateProvinceValue = async (newValue) => {
      province.value = newValue;
      await getDistricts({ province_id: newValue, basic: true, limit: 100 }, true);
      district.value = null;
      ward.value = null;
      wards.value = []
    };

    // Loading wards when district get new value
    const {
      isLoading: isLoadingWards,
      results: wards,
      getResults: getWards,
    } = useModelList("wards");

    const onUpdateDistrictValue = async (newValue) => {
      district.value = newValue;
      await getWards({ district_id: newValue, basic: true, limit: 100 }, true);
      ward.value = null;
    };

    const onUpdateWardValue = (newValue) => {
      ward.value = newValue;
    };

    const address = computed(() => {
      let rt = "";
      if (ward.value !== null) rt += getNameFromId(wards.value, ward.value, 3);
      if (district.value !== null) rt += ', ' + getNameFromId(districts.value, district.value, 2);
      if (province.value !== null) rt += ', ' + getNameFromId(provinces.value, province.value, 1);
      return rt;
    });

    const filterFunction = (value, query, item) => {
      if (value == null || query == null) return -1;

      return convertVietnamese(value.toString()).indexOf(
        convertVietnamese(query.toString())
      );
    };

    return {
      filterFunction,
      province,
      provinces,
      isLoadingProvinces,
      onUpdateProvinceValue,
      district,
      districts,
      isLoadingDistricts,
      onUpdateDistrictValue,
      ward,
      wards,
      isLoadingWards,
      onUpdateWardValue,
      address,
    };
  },
  delimiters: ['[[', ']]'],
});
app.use(vuetify).mount("#getAddress1");
