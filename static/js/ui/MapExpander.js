import geo from "../geo";

function MapExpander(root) {
  const mapEl = document.querySelector("#app-map");
  const articleHeaderEl = document.querySelector("#article-header");
  const initialMapHeight = mapEl.style.height;
  const initialMapHeightToggleLinkText = root.textContent;

  function toggleMapHeight(event) {
    event.preventDefault();
    if (mapEl.style.height === initialMapHeight) {
      try {
        window.scrollBy({
          top: articleHeaderEl.offsetTop - window.pageYOffset - 15,
          behavior: "smooth",
        });
      } catch (e) {}
      mapEl.style.height = "70vh";
      root.textContent = "Réduire la carte";
    } else {
      mapEl.style.height = initialMapHeight;
      root.textContent = initialMapHeightToggleLinkText;
    }
    geo.recalculateMapSize();
  }

  root.addEventListener("click", toggleMapHeight);
}

export default MapExpander;
