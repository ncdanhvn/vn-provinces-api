import { fetchApi, convertType } from "./utils.js";
const { ref } = Vue;

export default function useModelList(model) {
  const isLoading = ref(false);
  const results = ref([]);

  const getResults = async (params, alterNumberName = false) => {
    isLoading.value = true;
    const data = await fetchApi(model, params);
    if (data.results && Array.isArray(data.results)) {
      results.value = data.results;
    } else {
      console.error("The data format is not as expected.");
    }
    isLoading.value = false;

    if (alterNumberName) {
      alterName(model, results.value);
    }
  };

  return { isLoading, results, getResults };
}

function alterName(model, results) {
  // Convert name field of any result which can convert to number with prefix of its type
  // For example, 1 to 'district 1'
  let lv;
  if (model === "provinces") lv = 1;
  else if (model === "districts") lv = 2;
  else if (model === "wards") lv = 3;

  if (lv)
    results.forEach((rs) => {
      if (parseInt(rs.name)) {
        let type = convertType(rs.type, lv);
        if (type) {
          rs.name = type + " " + rs.name;
          rs.nameAltered = true;
        }
      }
    });
}
