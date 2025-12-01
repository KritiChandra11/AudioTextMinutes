Algorithm TLDR_Summarization
Input: file_input (audio/video/text)
Output: structured_summary (summary, decisions, action_items)

BEGIN
    # Step 1: Input Acquisition
    IF file_input.type == 'audio' OR 'video' THEN
        IF 'video' THEN
            audio_file ← extract_audio_from_video(file_input)
        ELSE
            audio_file ← file_input
        ENDIF
        transcript ← transcribe_audio(audio_file)
    ELSE
        transcript ← extract_text(file_input)
    ENDIF

    # Step 2: NLP Processing
    key_sentences ← PyTextRank(transcript)
    structured_prompt ← format_prompt(key_sentences)

    # Step 3: Abstractive Summarization
    response ← GeminiLLM(structured_prompt)
    json_output ← parse_json(response)

    # Step 4: Output Rendering
    display(transcript, json_output)
END
