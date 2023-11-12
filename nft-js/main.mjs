import Moralis from 'moralis';

try {
  await Moralis.start({
    apiKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6IjI0Mzc4NzgyLTNjZmItNDIwZS04ZjgyLWJkYTk0MjNhNmM0NyIsIm9yZ0lkIjoiMjI2MDQ0IiwidXNlcklkIjoiMjI2NDEwIiwidHlwZUlkIjoiOGFhMTA4ODctZjBiNi00YzNmLThlN2YtYTkxZjgyY2Q0OGQ2IiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE2OTc4NzY3NTQsImV4cCI6NDg1MzYzNjc1NH0.8DHNFny4xHmVK3eGDPXbzbRKdzG3VPE5-hqvQCCAJ3w"
  });

  const response = await Moralis.EvmApi.nft.getWalletNFTs({
    "chain": "0x89",
    "format": "decimal",
    "excludeSpam": true,
    "mediaItems": false,
    "address": "0xE21B74060Cdec9D96F865963d8e5F7Def37F0895"
//    "address": "0x3658DD5915A0a51394A4e5657cC2d3c5e7A141ED"
  });

  console.log(response.raw);
} catch (e) {
  console.error(e);
}
