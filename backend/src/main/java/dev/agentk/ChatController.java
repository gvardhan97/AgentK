package dev.agentk;
import java.util.Map;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestClient;
@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:3000")
public class ChatController {
 private final RestClient ai;
 public ChatController(@Value("${AI_SERVICE_URL:http://localhost:8000}") String url) {
  ai = RestClient.builder().baseUrl(url).build();
 }
 @PostMapping("/ask")
 public Map ask(@RequestBody Map<String,Object> body) {
  return ai.post().uri("/ask").body(body).retrieve().body(Map.class);
 }
}
