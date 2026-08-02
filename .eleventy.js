const { HtmlBasePlugin } = require("@11ty/eleventy");

module.exports = function (eleventyConfig) {
  eleventyConfig.addPlugin(HtmlBasePlugin);
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });
  eleventyConfig.addPassthroughCopy({ "src/CNAME": "CNAME" });

  eleventyConfig.addCollection("uebungen", (api) =>
    api.getFilteredByGlob("src/uebungen/*.md")
      .sort((a, b) => (a.data.title || "").localeCompare(b.data.title || "", "de"))
  );

  eleventyConfig.addCollection("einheiten", (api) =>
    api.getFilteredByGlob("src/einheiten/*.md")
      .sort((a, b) => (a.data.title || "").localeCompare(b.data.title || "", "de"))
  );

  eleventyConfig.addCollection("plaene", (api) =>
    api.getFilteredByGlob("src/plaene/*.md")
      .sort((a, b) => (a.data.title || "").localeCompare(b.data.title || "", "de"))
  );

  // Referenz-Auflösung: findet ein Collection-Item per Datei-Slug
  eleventyConfig.addFilter("bySlug", (items, slug) =>
    (items || []).find((i) => i.fileSlug === slug)
  );

  return {
    dir: { input: "src", includes: "_includes", data: "_data", output: "_site" },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk"
  };
};
