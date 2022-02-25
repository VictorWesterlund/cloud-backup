CREATE TABLE flags (
    k text PRIMARY KEY, 
    v real
);

CREATE TABLE fileindex (
    anchor text PRIMARY KEY,
    chksum text
);

INSERT INTO flags
VALUES
    ("CALC_CHECKSUM", 1),
    ("BUCKET_OK", 0);