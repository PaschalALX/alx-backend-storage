-- ranks country origins of bands, ordered by the 
-- number of (non-unique) fans

select origin, fans as nb_fans from metal_bands ORDER BY fans DESC;
