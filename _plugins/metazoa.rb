module Jekyll
  class MetazoaImageIndexing < Generator
    def generate(site)
      metazoa_loc = File.join(site.source, 'images/metazoa')
      site.data["metazoa"] = Dir[metazoa_loc + '/*'].map{|s| s.slice(site.source.length, s.length)}
    end
  end
end
