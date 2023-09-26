const { ref } = Vue;

// This function converts the string to lowercase, then perform the conversion
export function convertVietnamese(str) {
  str = str.toLowerCase();
  str = str.replace(/à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ/g, "a");
  str = str.replace(/è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ/g, "e");
  str = str.replace(/ì|í|ị|ỉ|ĩ/g, "i");
  str = str.replace(/ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ/g, "o");
  str = str.replace(/ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ/g, "u");
  str = str.replace(/ỳ|ý|ỵ|ỷ|ỹ/g, "y");
  str = str.replace(/đ/g, "d");
  str = str.replace(/\u0300|\u0301|\u0303|\u0309|\u0323/g, ""); // Huyền sắc hỏi ngã nặng
  str = str.replace(/\u02C6|\u0306|\u031B/g, ""); // Â, Ê, Ă, Ơ, Ư
  return str;
}

export async function fetchApi(path, parameters) {
  const baseUrl = "http://vnprovinces.pythonanywhere.com/api/";
  const url = new URL(path + "/?", baseUrl);

  if (parameters) {
    Object.keys(parameters).forEach((key) =>
      url.searchParams.append(key, parameters[key])
    );
  }

  let data;
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    data = await response.json();
  } catch (error) {
    console.error("Error fetching data:", error);
  }

  return data;
}

export function getNameFromId(items, id, level) {
  // Name should included type
  let rt = "";

  const item = items.find((i) => i.id === id);
  if (!item || !item.name) return rt;
  rt += item.name;

  // if item's name has been altered, then no need to add type as prefix
  if (item.nameAltered) return rt;

  let type = convertType(item.type, level);
  if (type) rt = type + " " + rt;
  return rt;
}

export function convertType(type, level) {
  let rt;
  if (level === 1)
    // province
    switch (type) {
      case "C":
        rt = "thành phố";
        break;
      case "P":
        rt = "tỉnh";
        break;
      default:
        break;
    }
  else if (level === 2)
    // district
    switch (type) {
      case "C":
        rt = "thành phố";
        break;
      case "UD":
        rt = "quận";
        break;
      case "RD":
        rt = "huyện";
        break;
      case "T":
        rt = "thị xã";
        break;
      default:
        break;
    }
  else if (level === 3)
    // ward
    switch (type) {
      case "W":
        rt = "phường";
        break;
      case "C":
        rt = "xã";
        break;
      case "T":
        rt = "thị trấn";
        break;
      default:
        break;
    }

  return rt;
}
