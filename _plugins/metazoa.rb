module Jekyll
  class MetazoaImageIndexing < Generator
    def generate(site)
      site.data["metazoa"] = Dir['images/metazoa/*'].map{|s| '/'+s}
    end
  end
end
