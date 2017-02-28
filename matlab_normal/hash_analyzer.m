
clear, clc, close all

[cont, list_hashes_hex] = textread('hashes1.txt','%d,%s');
j=1;
for i = 1:length(list_hashes_hex)
    if ~isempty(list_hashes_hex{i})
        list_hashes(j) = hex2dec(list_hashes_hex{i});
        j = j+1;
    end
end
        
media = mean(list_hashes)
mediana = median(list_hashes)
moda = mode(list_hashes)
desv_est = std(list_hashes,1)
varianza = var(list_hashes,1)
plot(abs(sort((list_hashes-moda))))