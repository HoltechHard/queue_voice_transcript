python python-clients/scripts/asr/transcribe_file.py \
    --server grpc.nvcf.nvidia.com:443 --use-ssl \
    --metadata function-id "a9eeee8f-b509-4712-b19d-194361fa5f31" \
    --metadata "authorization" "Bearer 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" \
    --language-code es-US \
    --input-file voice/test.ogg
