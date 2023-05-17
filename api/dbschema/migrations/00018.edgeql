CREATE MIGRATION m12ywt4td2bnp4dosbglvjohss4qeak3ro72dbcl4eytev4vhbs3nq
    ONTO m1laxia3ese7qqi3bvg3xsytv7eonouubsnvq47aosnxswwuuwlxka
{
  ALTER TYPE default::Status {
      ALTER PROPERTY title {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
